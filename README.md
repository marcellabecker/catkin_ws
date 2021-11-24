
# Turtlesim-setpoint-position

## Introdução
![banner](/pictures/1.jpg)

A atividade foi feita pelos voluntários do Laboratório ** RoSA - Robótica e Sistemas Autônomos ** durante o segundo período do ano letivo, 2021.2.

A proposta foi simular o movimento de uma tartaruga em um plano cartesiano a um ponto arbitrado pelo usuário **(x,y)**.


## Instalação
É necessário ter o **[ROS NOETIC](http://wiki.ros.org/noetic/Installation)** instalado na máquina para buildar.


### Criação de Workspace
Após instalado o **[ROS NOETIC](http://wiki.ros.org/noetic/Installation)**, crie um workspace.

```bash
$ mkdir -p ~/catkin_ws/src
```

### Repositório GitHub

clone o repositório.

```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/marcellabecker/turtle
``` 

### Build
Agora abra o terminal e navegue até a pasta **catkin_ws**.
```
$ cd ~/catkin_ws
``` 
Digite o comando: 
```
$ catkin_make
``` 
e o programa estará buildado.

### Roscore

Para que a simulação funcione corretamente, é preciso rodar um core.
**Em outro terminal**, digite:
```
$ roscore
``` 

![banner](/pictures/2.jpg)

### Run Node
Agora é necessário inicializar o node. Na pasta **catkin_ws** abra um novo terminal e digite o comando:

```
$ rosrun turtlesim turtlesim_node
``` 
![banner](/pictures/3.jpg)

### Setup
Na pasta catkin_wk. digite, **em outro terminal**, o comando:
```
$ source devel/setup.bash
``` 
Agora todas as funções estão carregadas.

### Run py file
Por fim digite:
```
$ rosrun turtle turtlechallenge.py
``` 
Aparecerá no console o input para arbitrar os valores de **x** e **y**.

### Vídeo

[![Video](resources/print.png)](https://youtu.be/NNkwSgDScuY)

## Informações para Contato
Caso deseje falar com os desenvolvedores do projeto seguem informações para contato:

**Alexandre Adonai**
- Email: alexandre.adonai@ieee.org
- GitHub: https://github.com/Alexandreaags
- LinkedIn: https://www.linkedin.com/in/alexandre-adonai-365a35211/

**Eduardo Lôbo Teixeira Filho**
- Email: eduardo.lobo@ieee.org
- GitHub: https://github.com/sirlobardo
- LinkedIn: https://www.linkedin.com/in/eduardo-l%C3%B4bo-8a4b961b3/

**Marcella Giovanna Santos**
- Email: marcella.santos@ieee.org
- GitHub: https://github.com/marcellabecker
- LinkedIn: https://www.linkedin.com/in/marcellagsantos

*“Do or do not. There is no try.”* - Mestre Yoda
