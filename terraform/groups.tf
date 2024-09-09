resource "azurerm_resource_group" "rg" {
  name     = "${local.prefix}${random_string.random.result}"
  location = var.default_location
  tags     = module.tags.tags
}
