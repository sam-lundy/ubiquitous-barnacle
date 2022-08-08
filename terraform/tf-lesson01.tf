	provider "aws" {
	  region = "us-east-1"
	}
	resource "aws_instance" "vm" {
	  ami           = "ami-0cabc39acf991f4f1"
	  subnet_id     = "subnet-0b0feb972f5d1ef53"
	  instance_type = "t3.micro"
	  tags = {
	    Name = "my-first-tf-node"
	  }
	}