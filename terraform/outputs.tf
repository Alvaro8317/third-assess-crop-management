output "webapp-outputs-ip-addresses" {
  value = azurerm_linux_web_app.webapp.outbound_ip_addresses
}

output "webapp-outputs-app-settings" {
  value = azurerm_linux_web_app.webapp.app_settings
}

output "webapp-outputs-site-config" {
  value     = azurerm_linux_web_app.webapp.site_config
  sensitive = true
}

output "ec2-public-ip" {
  value = module.aws.public_ip_instance
}
