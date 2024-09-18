resource "azurerm_storage_account" "storage_functions" {
  name                     = lower("alvaro8317${var.random}")
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  tags                     = module.tags.tags
}
