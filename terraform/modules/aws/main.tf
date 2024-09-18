resource "aws_instance" "suscriptor" {
  ami                    = var.ec2-specs.ami
  key_name               = aws_key_pair.aws_key_pair_solid.key_name
  instance_type          = var.ec2-specs.instance_type
  vpc_security_group_ids = [aws_security_group.suscriptor_sg.id]
  subnet_id              = aws_subnet.public_subnet.id
  user_data              = file("./scripts/user-data.sh")
  tags = {
    "Name" : "${var.prefix}suscriptor"
  }
}

resource "aws_key_pair" "aws_key_pair_solid" {
  key_name   = "deployer_key"
  public_key = file("~/.ssh/id_terraform.pub")
  tags = {
    "Name" = "${var.prefix}key-pair"
  }
}


