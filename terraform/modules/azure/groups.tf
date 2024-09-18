resource "azurerm_resource_group" "rg" {
  name     = "${var.prefix}${var.random}"
  location = var.default_location
  tags     = module.tags.tags
}
