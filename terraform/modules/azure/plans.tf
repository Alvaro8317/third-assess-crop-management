resource "azurerm_service_plan" "appserviceplan" {
  name                = "${var.prefix}plan-service-${var.random}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "B1"
  tags                = module.tags.tags
}
