module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.0.0"

  cluster_name    = var.cluster_name
  cluster_version = "1.29"

  vpc_id     = var.vpc_id
  subnet_ids = var.private_subnets

  cluster_endpoint_public_access = true

  eks_managed_node_groups = {
    default = {
      min_size       = 1
      max_size       = 3
      desired_size   = var.desired_nodes
      instance_types = [var.node_instance_type]

      labels = {
        Environment = "dev"
      }
    }
  }

  tags = {
    Environment = "dev"
    Project     = "devops-project"
  }
}
