module "tags" {
  source = "./modules/tags"
  additional_tags = {
    Service = "AppService"
  }
}

resource "azurerm_service_plan" "appserviceplan" {
  name                = "${local.prefix}plan-service-${random_string.random.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "B1"
  tags                = module.tags.tags
}

resource "azurerm_linux_web_app" "webapp" {
  name                = "${local.prefix}webapp-${random_string.random.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  service_plan_id     = azurerm_service_plan.appserviceplan.id
  https_only          = true
  site_config {
    app_command_line    = "python src/app.py "
    minimum_tls_version = "1.2"
    application_stack {
      python_version = "3.12"
    }
  }
  app_settings = {
    python_version = "3.12"
  }
  tags = module.tags.tags
}

resource "azurerm_app_service_source_control" "sourcecontrol" {
  app_id                 = azurerm_linux_web_app.webapp.id
  repo_url               = "https://github.com/Alvaro8317/third-assess-crop-management.git"
  branch                 = "main"
  use_manual_integration = true
  use_mercurial          = false
}
