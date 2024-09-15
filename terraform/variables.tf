variable "default_location" {
  type        = string
  description = "Default location to deploy the resources"
  default     = "eastus2"

}

variable "ubidots_token" {
  type        = string
  description = "Ubidots token to MQTT Broker"
}

variable "tags_aws" {
  description = "Tags of AWS"
  type        = map(string)
}
