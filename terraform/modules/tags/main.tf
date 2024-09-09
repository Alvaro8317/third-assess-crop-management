variable "additional_tags" {
  type    = map(string)
  default = {}
}

output "tags" {
  value = merge(
    {
      Environment = "Development"
      Project     = "ThirdAssessment"
      Service     = "CropManagement"
    },
    var.additional_tags
  )
}
