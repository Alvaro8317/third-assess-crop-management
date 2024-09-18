module "aws" {
  source = "./modules/aws"
  prefix = local.prefix
}

module "azure" {
  source        = "./modules/azure"
  prefix        = local.prefix
  ubidots_token = var.ubidots_token
  random        = random_string.random.result
}
