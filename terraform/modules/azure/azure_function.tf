resource "azurerm_application_insights" "application_insight" {
  name                = "${var.prefix}-app-insight"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.default_location
  application_type    = "other"
  tags                = module.tags.tags
}

resource "azurerm_linux_function_app" "mocker_crop_sensors" {
  functions_extension_version = "~4"
  https_only                  = true
  location                    = azurerm_resource_group.rg.location
  name                        = "${var.prefix}mocker-crop-${var.random}"
  resource_group_name         = azurerm_resource_group.rg.name
  service_plan_id             = azurerm_service_plan.appserviceplan.id
  storage_account_access_key  = azurerm_storage_account.storage_functions.primary_access_key
  storage_account_name        = azurerm_storage_account.storage_functions.name
  site_config {
    always_on = true
    application_stack {
      python_version = "3.11"
    }
  }
  app_settings = {
    FUNCTIONS_WORKER_RUNTIME         = "python"
    "ENABLE_ORYX_BUILD"              = "true"
    "SCM_DO_BUILD_DURING_DEPLOYMENT" = "true"
    "AzureWebJobsFeatureFlags"       = "EnableWorkerIndexing"
    "APPINSIGHTS_INSTRUMENTATIONKEY" = azurerm_application_insights.application_insight.instrumentation_key
    "UBIDOTS_TOKEN"                  = var.ubidots_token
  }
  tags = module.tags.tags
}
