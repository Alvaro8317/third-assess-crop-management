resource "aws_vpc" "main_vpc" {
  cidr_block = var.vpc-specs.cidr_vpc
  tags = {
    "Name" = "${var.prefix}VPC"
  }
}
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = cidrsubnet(aws_vpc.main_vpc.cidr_block, 8, 1)
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"
  tags = {
    "Name" = "${var.prefix}pub-subnet"
  }
}

resource "aws_subnet" "public_subnet2" {
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = cidrsubnet(aws_vpc.main_vpc.cidr_block, 8, 2)
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1b"
  tags = {
    "Name" = "${var.prefix}pub-subnet2"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main_vpc.id
  tags = {
    "Name" = "${var.prefix}igw"
  }
}
resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.main_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
  tags = {
    "Name" = "${var.prefix}route-tb"
  }
}

resource "aws_route_table_association" "subnet1_association" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_route_table_association" "subnet2_association" {
  subnet_id      = aws_subnet.public_subnet2.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_security_group" "suscriptor_sg" {
  name        = "${var.prefix}-SG"
  description = "Allow access SSH"
  vpc_id      = aws_vpc.main_vpc.id
  dynamic "ingress" {
    for_each = [22, 80, 443]
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "${var.prefix}SG"
  }
}
