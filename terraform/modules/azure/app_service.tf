module "tags" {
  source = "../tags"
  additional_tags = {
  }
}

resource "azurerm_container_registry" "acr" {
  name                = "cropContainerRegistry"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_linux_web_app" "webapp" {
  enabled                       = true
  https_only                    = true
  location                      = azurerm_resource_group.rg.location
  name                          = "${var.prefix}webapp-${var.random}"
  public_network_access_enabled = true
  resource_group_name           = azurerm_resource_group.rg.name
  service_plan_id               = azurerm_service_plan.appserviceplan.id
  lifecycle {
    prevent_destroy = true
  }
  site_config {
    application_stack {
      docker_image_name        = "crop-management:latest"
      docker_registry_url      = "https://${azurerm_container_registry.acr.login_server}"
      docker_registry_username = azurerm_container_registry.acr.admin_username
      docker_registry_password = azurerm_container_registry.acr.admin_password
    }
    always_on                               = true
    app_command_line                        = "fastapi run --host 0.0.0.0 --port 8000"
    container_registry_use_managed_identity = false
    load_balancing_mode                     = "LeastRequests"
    minimum_tls_version                     = "1.2"
  }
  app_settings = {
    DOCKER_ENABLE_CI                    = true
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = "false"
  }
  tags = module.tags.tags
}
