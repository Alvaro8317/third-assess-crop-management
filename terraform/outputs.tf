output "ec2-public-ip" {
  value = module.aws.public_ip_instance
}

output "URLCropManagement" {
  value = module.azure.URLCropManagement
}
