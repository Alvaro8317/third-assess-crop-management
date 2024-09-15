terraform {
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = "3.6.2"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.1.0"
    }
    aws = {
      source  = "hashicorp/aws"
      version = "5.67.0"
    }
  }
  required_version = ">= 0.14.9"
}
provider "azurerm" {
  subscription_id = "d3d1dd8e-5766-4302-938f-c80e2b523e64"
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
}

provider "aws" {
  region = "us-east-1"
  default_tags {
    tags = var.tags_aws
  }
}
