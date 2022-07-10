#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/time.h>
#include <errno.h>
#include <time.h>
#define FALSE 0
#define TRUE 1
#define PARADO 0
#define CIMA 1
#define BAIXO -1
void init_building(void);
//Elevador
void init_elevador(void);
void init_people(int,int);
void finish(void);
int next_dest(int, int, int, int);
void open_door(int,int);
void close_door(int,int);
void press_button(int);
int wait(int,int);
void get_in(int,int,int,int);
void go_on(int,int,int);
void get_out(int,int,int);
// # //################################ Fim
// # Prototipos#####################################################################
// # //################################ ESTRUTURAS
// # #####################################################################
typedef struct
{
    int n_elev;//nº do elevador
    int pisoActual;// piso em que o elevador se encontra
    int pisoChegada;//piso de destino do elevador
    int direccao;//Cima,Baixo,Parado
    int direccao_ant;
}Elevador;
typedef struct
{
    int n_pess;
    int pisoDestino;
    int elev;
}Pessoa;
typedef struct
{
    float tempoMedioEspera;
    float tempoMedioViagem;
    int tempoMaximoEspera;
    int tempoMaximoViagem;
}Estatistica; 
// // ####################### FIM ESTRUTURAS
// ########################################################################## // ################################ Threads
// ########################################################################
void *thr_elevador(void *params);
void *thr_pessoa(void *arg);
pthread_mutex_t *muxPortaElevadores;
pthread_mutex_t *muxPainelChamada;
pthread_mutex_t *muxBotaoChamada;
pthread_mutex_t *muxPisoAtendido;
pthread_cond_t elev_cond;
// # //################################ Fim Threads
// # ################################################################
// # //################################ Globais
// # ####################################################################
# //Variaveis de representação do estado do edificio
int **portaElevadores;//Vector que contem Vectores em que o id do elevador corresponde a sua posição no
int *botaoChamada;//vector que contem o estado de chamada do botao, a posição de cada estado corresponde ao
int **painelChamada;//vector que contem vectores de booleanos que indicam o piso accionado (um por
int **pisoAtendido;
//Global para puder pesquisar o painel de controlo do elevador
int num_floors;
int num_elevators;
int num_people;
int speed;
int waitt;
int workt;
//Variavel de controlo de final de simulação
int finished=0;
pthread_t *elevator_t;
pthread_t *people_t;
// # //################################ Fim Globais
// # ################################################################
// # /***************************************************************************************
// # PROGRAMA PRINCIPAL
// # ***************************************************************************************/
int main(int argc, char *argv[])
{
//Threads ID's -> Servem para identificação de cada um dos threads
//pthread_t *tid;
//Teste de USAGE!!!
if(argc != 9)
{
printf ("USAGE : simelev nfloors nelev nusers speed waitt intmin intmax workt\n");
return -1;
}
srand(time(NULL));
// declaração de variáveis
// o espaço para algumas das variáveis deverá ser alocado dinamicamente
num_floors=atoi(argv[1]);
num_elevators=atoi(argv[2]);
num_people=atoi(argv[3]);
speed=atoi(argv[4]);
waitt=atoi(argv[5]);
int intmin=atoi(argv[6]);
int intmax=atoi(argv[7]);
workt=atoi(argv[8]);
if(intmax<intmin)
{
printf("USAGE: intmin tem de ser inferior a intmax!!\n");
return -1;
}
//int esperaPessoa=(int) argv[2];;
init_building();
init_elevador();
init_people(intmin,intmax);
finish();
pthread_exit(NULL);//Espera pela terminação dos seus THREADS;
}
void init_building()
    {
    int i;
    pthread_cond_init (&elev_cond,NULL);
    portaElevadores = calloc(num_floors, sizeof(int*));
    for(i=0; i<num_floors; i++)
        portaElevadores[i]= calloc(num_elevators , sizeof(int));
        painelChamada = calloc(num_elevators,sizeof(int*));
    for(i=0; i<num_elevators; i++)
        painelChamada[i]= calloc(num_floors , sizeof(int));
        portaPisos = (int*) malloc(num_floors*sizeof(int));
        botaoChamada = (int*) caprintf("Elevador %d a subir do piso %d para o piso %d\n",elev.n_elev,elev.pisoActual,elev.pisoChegada);lloc (num_floors,
        sizeof(int));
        botaoChamada = (int*) calloc (num_floors, sizeof(int));
        pisoAtendido = calloc (num_floors, sizeof(int*));
    for(i=0; i<num_floors;i++)
    {
        pisoAtendido[i] = calloc (2, sizeof(int));
    }
    muxPisoAtendido = calloc (num_floors,sizeof(pthread_mutex_t));
    muxPortaElevadores = calloc (num_floors,sizeof(pthread_mutex_t));
    muxBotaoChamada = calloc (num_floors,sizeof(pthread_mutex_t));
    for(i=0;i<num_floors;i++)
    {
        pthread_mutex_init (&(muxPortaElevadores[i]),NULL);
        pthread_mutex_init (&(muxBotaoChamada[i]),NULL);
    }
    muxPainelChamada = (pthread_mutex_t*) malloc (num_elevators*sizeof(pthread_mutex_t));
    for(i=0;i<num_elevators;i++)
    {
        pthread_mutex_init (&(muxPainelChamada[i]),NULL);
    }
}
void init_elevador()
{
//pthread_t elevator_t[num_elevators];
elevator_t = calloc(num_elevators,sizeof(pthread_t));
int i;
for(i=0;i<num_elevators;i++)
{
pthread_create(&elevator_t[i], NULL, thr_elevador, (void *) i);// foi usado o
"truque dos acetatos passamos o valor do argumento em vez de se passar o seu endereço"
}
}
void init_people(int intmin,int intmax)
{
//pthread_t people_t[num_people];
people_t = calloc(num_people,sizeof(pthread_t));
int i;
int esperaPessoa;
for (i=0;i<num_people;i++)
{
printf("[CRIADA] Pessoa %d foi criada\n", i);
pthread_create(&people_t[i], NULL, thr_pessoa, (void *) i);
esperaPessoa = rand()%(intmax+1-intmin)+intmin;
//printf("Tempo de espera da pessoa criada = %d\n",esperaPessoa);
//printf("Tempo maximo de espera para pessoa criada = %d\n",intmax);
sleep(esperaPessoa);
}
}
void finish()
{
int i;
void *tempoEspera[num_people-1];
Estatistica stat;
//float tempoEsperaMedio;
for(i=0;i<num_people;i++)
{
pthread_join(people_t[i],&tempoEspera[i]);
//tempoEsperaTotal=tempoEsperaTotal + *(Estatistica *) tempoEspera[i];
//stat = *(Estatistica *) tempoEspera[i];
//printf("[Acabou] A pessoa %d com um tempo de espera por elevadores medio de %f
segundos!!!\n",i+1,stat.tempoMedioEspera);
}
finished=1;
for(i=0;i<num_people;i++)
{
pthread_join(elevator_t[i],NULL);
}
//Apresenta a estatistica da simulação
printf("\n");
printf("########################## ESTATISTICAS ##########################\n");
printf("Pessoa\tTempo Medio de Espera\tTempo Medio de Viagem\tTempo Maximo de
Espera\tTempo Maximo de Viagem\n");
float tempoMedioEsperaTotal=0;
float tempoMedioViagemTotal=0;
float tempoMaximoEsperaTotal=0;
float tempoMaximoViagemTotal=0;
for(i=0;i<num_people;i++)
{
stat = *(Estatistica *) tempoEspera[i];
printf("%d \t%f \t%f \t%d \t%d\n",
i,stat.tempoMedioEspera,stat.tempoMedioViagem,stat.tempoMaximoEspera,stat.tempoMaximoViagem);
tempoMedioEsperaTotal= (tempoMedioEsperaTotal+stat.tempoMedioEspera);
tempoMedioViagemTotal=(tempoMedioViagemTotal+stat.tempoMedioViagem);
tempoMaximoEsperaTotal=(tempoMaximoEsperaTotal + stat.tempoMaximoEspera);
tempoMaximoViagemTotal=(tempoMaximoViagemTotal + stat.tempoMaximoViagem);
}
printf("Media:\t%f \t%f \t%f \t%f\n",
tempoMedioEsperaTotal/num_people,tempoMedioViagemTotal/num_people,tempoMaximoEsperaTotal/num_people,tempoMa
ximoViagemTotal/num_people);
printf("##################### Fim das ESTATISTICAS #######################\n");
/*for(i=0;i<num_people;i++)
{
}*/
}
// # /**********************************************************************************************************
// # ***********
// # ELEVADOR
// # ***********************************************************************************************************
// # **********/
void *thr_elevador(void *arg)
{
Elevador elev;
int id;
id=(int) arg;
elev.n_elev = id+1;
elev.pisoActual=0;
elev.pisoChegada=0;
elev.direccao=PARADO;
elev.direccao_ant=PARADO;
//sleep(2);
/*pthread_mutex_lock(&muxPortaElevadores[elev.pisoActual]);
printf("Estado da porta do elevador nº %d: %d\n", elev.n_elev,
portaElevadores[elev.pisoActual][id]);
pthread_mutex_unlock(&muxPortaElevadores[elev.pisoActual]);*/
//int i;
while(1)
{
//printf("Varios YEHS YEHHHH!!!\n");
pthread_mutex_lock(&muxPainelChamada[id]);
pthread_mutex_lock(&muxBotaoChamada[elev.pisoActual]);
pthread_mutex_lock(&muxPisoAtendido[elev.pisoActual]);
elev.pisoChegada = next_dest(id ,elev.pisoActual,elev.direccao,elev.direccao_ant);
pthread_mutex_unlock(&muxPisoAtendido[elev.pisoActual]);
pthread_mutex_unlock(&muxBotaoChamada[elev.pisoActual]);
pthread_mutex_unlock(&muxPainelChamada[id]);
if(elev.pisoActual == elev.pisoChegada)
{
if (elev.direccao != PARADO)
{
printf("\t[PARAR] Elevador %d parou no piso
%d\n",elev.n_elev,elev.pisoActual);
elev.direccao_ant=elev.direccao;
elev.direccao=PARADO;
}
open_door(id,elev.pisoActual);
sleep(waitt);//tempo de espera com a porta aberta
} else if(elev.pisoActual < elev.pisoChegada)
{
if(elev.direccao != CIMA)
{
elev.direccao=CIMA;
close_door(id,elev.pisoActual);
printf("\t[SUBIR] Elevador %d a subir do piso %d para o piso
%d\n",elev.n_elev,elev.pisoActual,elev.pisoChegada);
}
elev.pisoActual++;
sleep(speed);//tempo de espera entre pisos
}else
{
if(elev.direccao != BAIXO)
{
elev.direccao=BAIXO;
close_door(id,elev.pisoActual);
printf("\t[DESCER] Elevador %d a descer do piso %d para o piso
%d\n",elev.n_elev,elev.pisoActual,elev.pisoChegada);
}
elev.pisoActual--;
sleep(speed);//tempo de espera entre pisos
}
if(finished==1)
return NULL;
}
return NULL;
}
int next_dest(int id_Elevador, int pisoActual, int direccao, int direccao_ant)
{
int i;
if(direccao == PARADO || direccao == CIMA)
{
//Verifica Para Pisos superiores
if(direccao == PARADO && direccao_ant == BAIXO )
{
int k;
for(k=pisoActual;k>=0;k--)
{
if(painelChamada[id_Elevador][k] == TRUE)
return k;
if(botaoChamada[k] == TRUE && ((pisoAtendido[k][0] == FALSE) ||
(pisoAtendido[k][0] == TRUE && pisoAtendido[k][1] == id_Elevador )))
{
pisoAtendido[k][0] = TRUE;
pisoAtendido[k][1] = id_Elevador;
return k;
}
}
}
for (i=pisoActual;i<num_floors;i++)
{
if(painelChamada[id_Elevador][i] == TRUE )
return i;
if(botaoChamada[i] == TRUE && ((pisoAtendido[i][0] == FALSE) ||
(pisoAtendido[i][0] == TRUE && pisoAtendido[i][1] == id_Elevador )))
{
pisoAtendido[i][0] = TRUE;
pisoAtendido[i][1] = id_Elevador;
return i;
}
}
//Se nao encontrar verifica para pisos inferiores
for (i=pisoActual;i>=0;i--)
{
if(painelChamada[id_Elevador][i] == TRUE)
return i;
if(botaoChamada[i] == TRUE && ((pisoAtendido[i][0] == FALSE) ||
(pisoAtendido[i][0] == TRUE && pisoAtendido[i][1] == id_Elevador )))
{
pisoAtendido[i][0] = TRUE;
pisoAtendido[i][1] = id_Elevador;
return i;
}
}
}
if(direccao==BAIXO)
{
//Verifica Para Pisos inferiores
for (i=pisoActual;i>=0;i--)
{
if(painelChamada[id_Elevador][i] == TRUE)
return i;
if(botaoChamada[i] == TRUE && ((pisoAtendido[i][0] == FALSE) ||
(pisoAtendido[i][0] == TRUE && pisoAtendido[i][1] == id_Elevador )))
{
pisoAtendido[i][0] = TRUE;
pisoAtendido[i][1] = id_Elevador;
return i;
}
}
//Se nao encontrar verifica para pisos superiores
// for (i=pisoActual;i<num_floors;i++)
// {
// if(painelChamada[id_Elevador][i] == TRUE)
// return i;
// if(botaoChamada[i] == TRUE)
// return i;
//
// }
}
return pisoActual;
}
void open_door(int id,int pisoActual)
{
pthread_mutex_lock(&muxPortaElevadores[pisoActual]);
if(portaElevadores[pisoActual][id] == FALSE)
{
printf("[ABRIR] O elevador nº %d abriu a porta\n", id+1);
portaElevadores[pisoActual][id]= TRUE;
}
pthread_mutex_unlock(&muxPortaElevadores[pisoActual]);
pthread_cond_broadcast(&elev_cond);
}
void close_door(int id, int pisoActual)
{
pthread_mutex_lock(&muxPortaElevadores[pisoActual]);
printf("[FECHAR] O elevador nº %d fechou a porta\n", id+1);
portaElevadores[pisoActual][id]= FALSE;
pthread_mutex_unlock(&muxPortaElevadores[pisoActual]);
}
# /**********************************************************************************************************
# ***********
# PESSOA
# ***********************************************************************************************************
# **********/
# //definição das funções
# //fim da definição
# //funçoes
void press_button(int piso)
{
pthread_mutex_lock(&muxBotaoChamada[piso]);
botaoChamada[piso]=TRUE;
pthread_mutex_unlock(&muxBotaoChamada[piso]);
}
int wait(int id,int piso)
{
int i;
//int tempoEspera;
pthread_mutex_lock(&muxPortaElevadores[piso]);
for (i=0;i<=num_elevators;i++)
{
if (portaElevadores[piso][i] == TRUE)
{
printf("[ABRIR] Porta aberta do elevador %d no piso %d\n",i+1,piso);
pthread_mutex_unlock(&muxPortaElevadores[piso]);
return i;
}
}
printf("\t[WAIT] Pessoa %d esperando...\n",id+1);
while(1)
{
press_button(piso);
pthread_cond_wait(&elev_cond,&muxPortaElevadores[piso]);
for (i=0;i<=num_elevators;i++)
{
if (portaElevadores[piso][i] == TRUE)
{
printf("[ABRIR] Porta aberta do elevador %d no piso
%d\n",i+1,piso);
pthread_mutex_unlock(&muxPortaElevadores[piso]);
return i;
}
}
}
}
void get_in(int id,int elevador,int destino,int piso)
{
pthread_mutex_lock(&muxBotaoChamada[piso]);
pthread_mutex_lock(&muxPisoAtendido[piso]);
botaoChamada[piso]=FALSE;
pisoAtendido[piso][0]=FALSE;
pthread_mutex_unlock(&muxPisoAtendido[piso]);
pthread_mutex_unlock(&muxBotaoChamada[piso]);
pthread_mutex_lock(&muxPainelChamada[elevador]);
painelChamada[elevador][destino] = TRUE;
pthread_mutex_unlock(&muxPainelChamada[elevador]);
printf("\t[ENTRAR] Pessoa %d entrou no elevador %d\n",id+1,elevador+1);
}
void go_on(int id,int elev,int destino)
{
pthread_mutex_lock(&muxPortaElevadores[destino]);
while(1)
{
pthread_cond_wait(&elev_cond,&muxPortaElevadores[destino]);
if (portaElevadores[destino][elev] == TRUE)
{
printf("[CHEGAR] Pessoa %d chegou ao piso %d\n",id+1,destino);
pthread_mutex_unlock(&muxPortaElevadores[destino]);
return;
}
}
}
void get_out(int id,int elevador,int destino)
{
pthread_mutex_lock(&muxPainelChamada[elevador]);
painelChamada[elevador][destino] = FALSE;
pthread_mutex_unlock(&muxPainelChamada[elevador]);
printf("[CHEGAR] Pessoa %d saiu do elevador %d no piso %d\n",id+1,elevador+1,destino);
}
void *thr_pessoa(void *arg)
{
Pessoa pess;
Estatistica stats;
int id;
int piso;
void *stat;
time_t firstArrival, firstDeparture,secondArrival,
secondDeparture,firstStartJourney,firstFinishJourney,secondStartJourney,secondFinishJourney;
id = (int) arg;
pess.n_pess = id+1;
pess.pisoDestino = rand()%(num_floors-1)+1;
//Quer ir para o piso desejado
time(&firstArrival);
pess.elev= wait(id,0);
time(&firstDeparture);
//printf("fim do primeiro wait\n");
get_in(id,pess.elev,pess.pisoDestino,0);
time(&firstStartJourney);
go_on(id,pess.elev,pess.pisoDestino);
time(&firstFinishJourney);
get_out(id,pess.elev,pess.pisoDestino);
printf("\t[WORKING] Pessoa %d está a trabalhar no piso %d\n",id+1,pess.pisoDestino);
//Chegou a Piso Desejado
sleep(workt);
//Quer Sair do Edificio
piso = pess.pisoDestino;
pess.pisoDestino = 0;
pess.elev=wait(id,piso);
time(&secondDeparture);
get_in(id,pess.elev,0,piso);
time(&secondStartJourney);
go_on(id,pess.elev,0);
time(&secondFinishJourney);
get_out(id,pess.elev,0);
int firstWait = (int)(firstDeparture-firstArrival);
int secondWait = (int)(secondDeparture-secondArrival);
int firstJourney = (int)(firstFinishJourney-firstStartJourney);
int secondJourney = (int)(secondFinishJourney-secondStartJourney);
stats.tempoMedioEspera = ((float)firstWait + (float)secondWait)/2;
stats.tempoMedioViagem = ((float)firstJourney + (float)secondJourney)/2;
if(firstWait >= secondWait)
stats.tempoMaximoEspera = firstWait;
else
stats.tempoMaximoEspera = secondWait;
if(firstJourney >= secondJourney)
stats.tempoMaximoViagem = firstJourney;
else
stats.tempoMaximoViagem = secondJourney;
stat = malloc(sizeof(Estatistica));
*(Estatistica *) stat = stats;
return stat;