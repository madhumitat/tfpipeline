resource "azurerm_resource_group" "prereq_rg" {
  name     = "rg_tfprereq"
  location = "North Europe"
}

resource "azurerm_storage_account" "terraformstate" {
  name                     = "terraformstatecatone"
  resource_group_name      = azurerm_resource_group.prereq_rg.name
  location                 = azurerm_resource_group.prereq_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "tfstate" {
  name                  = "tfstate"
  storage_account_name  = azurerm_storage_account.terraformstate.name
  container_access_type = "private"
}