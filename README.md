
# Turtlesim-setpoint-position

## Introdução
![banner](/pictures/1.jpg)

A atividade foi feita pelos voluntários do Laboratório **BIR - Brazilian in Robotics** durante o segundo período do ano letivo - 2021.2.

A proposta foi simular o movimento de uma tartaruga do ponto cartesiano **(0,0)** a um ponto arbitrado pelo usuário **(x,y)**.

## Organização
A organização das pastas é a seguinte:

- `src/` - Contém a pasta *turtle*.

- `src/turtle` - Contém a pasta *scripts*, arquivo CMAkeLists.txt e package.xml. 
  
- `src/turtle/scripts` - Contêm o script *turtlechallenge.py*, o qual será buildado.


## Instalação
É necessário ter o **[ROS NOETIC](http://wiki.ros.org/noetic/Installation)** instalado na máquina para buildar.


### Repositório GitHub
Após instalado o **[ROS NOETIC](http://wiki.ros.org/noetic/Installation)**, clone o repositório.

```
$ git clone https://github.com/marcellabecker/catkin_ws
``` 

### Build
Agora abra o terminal e navegue até a pasta **catkin_ws**.
```
$ cd https://github.com/marcellabecker/catkin_ws
``` 
Digite o comando: 
```
$ catkin_make
``` 
e o programa estará buildado.

### Roscore
Para que a simulação funcione corretamente é preciso rodar um core.
**Em outro terminal**, digite:
```
$ roscore
``` 

### Run Node
Agora é necessário inicializar o node. Na pasta **catkin_wk** abra um terminal e digite:

```
$ rosrun turtlesim turtlesim_node
``` 
### Setup
Na pasta catkin_wk. digite, **em outro terminal**, o comando:
```
$ source devel/setup.bash
``` 
Agora todas as funções estão carregadas.

### Run py file
Por fim digite:
```
$ rosrun turtlechallenge.py
``` 
Aparecerá no console o input para arbitrar os valores de **x** e **y**.

## Informações para Contato
Caso deseje falar com os desenvolvedores do projeto seguem informações para contato:

**Alexandre Adonai**
- Email: alexandre.s@aln.senaicimatec.edu.br
- GitHub: https://github.com/Alexandreaags

**Eduardo Lôbo Teixeira Filho**
- Email: eduardo.lobo@ieee.org
- GitHub: https://github.com/sirlobardo
- LinkedIn: https://www.linkedin.com/in/eduardo-l%C3%B4bo-8a4b961b3/

**Marcella**
- Email: 
- GitHub: https://github.com/marcellabecker
- LinkedIn: https://www.linkedin.com/in/marcella-santos-b20b42161/

*“Fazer ou não fazer. Tentativa não há”* - Mestre Yoda
