variable "ubidots_token" {
  type = string
}
variable "default_location" {
  type        = string
  description = "Default location to deploy the resources"
  default     = "eastus2"
}

variable "prefix" {
  type = string
}

variable "random" {
  type = string
}
