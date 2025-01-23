terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "flask_network" {
  name = "flask_network"
}

resource "docker_image" "flask_image" {
  name = "flask_app"
  build {
    context = "."
  }
}

resource "docker_container" "flask_app" {
  name  = "flask_app"
  image = docker_image.flask_image.name
  ports {
    internal = 5000
    external = 5000
  }
  networks_advanced {
    name = docker_network.flask_network.name
  }
  env = [
    "REDIS_URL=redis://redis:6379/0"
  ]
  depends_on = [docker_image.flask_image]
}

resource "docker_container" "redis" {
  name  = "redis"
  image = "redis:alpine"
  ports {
    internal = 6379
    external = 6379
  }
  networks_advanced {
    name = docker_network.flask_network.name
  }
}
