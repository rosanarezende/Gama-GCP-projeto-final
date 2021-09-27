# Gama-GCP-projeto-final
Projeto Final apresentado no curso de Google Cloud Plataform da Gama Academy em parceria com a Magazine Luiza


<br><br>

## Instruções para rodar o projeto

O pré-requisito é ter o docker instalado na sua máquina:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install)

<br>

Com o docker rodando, use o comando:

```bash
docker-compose up
```

O projeto estará rodando no [http://localhost:8000/](http://localhost:8000/)

<br><br>

## Instruções para rodar o Kubernetes

São pré-requisitos ter o Kubernetes (kubectl) e o Minikube instalados na sua máquina:
- [Kubernetes](https://kubernetes.io/releases/download/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

<br>

O primeiro passo é baixar a imagem do nosso projeto no [dockerhub](https://hub.docker.com/r/samaraborges/gama-gcp-projeto-final):


```bash
docker pull samaraborges/gama-gcp-projeto-final:v1
```

E rodá-la na sua máquina:

```bash
docker run -d -p 8000:8000 -it samaraborges/gama-gcp-projeto-final:v1
```

Em seguida, rodando o terminal na pasta do projeto, é necessário:

- iniciar o Kubernetes na máquina
  ```bash
  minikube start
  ```

- pedir para que ele leia o arquivo arquivo criado no projeto
  ```bash
  kubectl apply -f deployment.yaml
  ```

- inclir a imagem no minikube:
  ```bash
  docker save samaraborges/gama-gcp-projeto-final:v1 | (eval $(minikube docker-env) && docker load)
  ```

- e solicitar que ele abra o dashboard
  ```bash
  minikube dashboard
  ```

Finalmente, quando o dashboard abrir no navegador, escolha a opção "kube-system".

![kubernetes](https://user-images.githubusercontent.com/45580434/134909257-cd5ee158-c093-4372-804f-ece27989e8bc.png)

<br><br>