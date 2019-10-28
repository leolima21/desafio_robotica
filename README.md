
PROCESSO SELETIVO – PROGRAMA NOVOS TALENTOS
=============================================

Este repositorio contem todos os aquivos gerados pelo candidato LEONARDO MENDES DE SOUZA LIMA, referentes ao desafio proposto pelo programa. Devido a alguns problemas, o desafio nao foi completamente solucionado mas por meio deste arquivo poderei explicar a ideia principal que tive e os problemas que encontrei no desenvolvimento da solucao.


==============================================
1.0 IDEIA PRINCIPAL PARA A SOLUCAO DO PROBLEMA
==============================================

1.1 Mapeamento:
Tendo em vista o tempo de 2 minutos para a execucao da missao, era necessario que o quadcopter se movimentasse pelo labirinto de forma bastante objetiva, sem perder muito tempo na exploracao do ambiente. Entao, decidi integrar o Hector SLAM ao quadricoptero para fazer o mapeamento da regiao apresentada.  

1.2 Busca:
Na missao nao havia tempo para simplesmente andar aleatoriamente no labirinto ate encontrar o alvo. Para conluir a tempo eu precisava garantir que  o quadricoptero nao iria passar 2 ou mais vezes pelo mesmo lugar. Usando o mapa gerado pelo SLAM a logica era navegar sempre por areas que ainda nao eram conhecidas pelo robo, desta maneira o robo nao iria perder tempo voando repetidas vezes pelo mesmo local.

1.3
Visao:
A ideia desta parte do projeto era criar nos no ROS, respectivamente inscritos nos topicos que estariam recebendo as imagens das cameras frontal, traseira e inferior. o codigo foi inscrito em Python e usa um classificador Haar cascade para identificar a caixa preta. No momento da identificacao, o programa iria desenhar um quadrado vermelho em volta da caixa e pausaria a execucao de todo o projeto.

1.4
Ideia alternativa:
Uma ideia alternativa a apresentada acima era usar o recurso path finding para gerar um caminho de forma automatica. Regulando a area de acao da ferramenta seria possivel simular sensores e ao mesmo tempo fazer o quadricoptero se movimentar de forma aleatoria pelo mapa. O ponto de chegada do caminho seria alternado atraves de pontos aleatorios.


==============================================
2.0 PROBLEMAS ENCONTRADOS
==============================================

2.1 Falta de conhecimento com o software V-REP:
Por ser a primeira vez utilizando o software em questao, a maior parte do tempo de trabalho foi realmente aprender a usar o programa. O mesmo possui poucos meios de aprendizado na internet e recentemente o forum do simulador passou por diversos tipos de SPAM e por isso nao estava permitindo que novos usuarios criassem topicos sem antes passar por uma aprovacao de um moderador na primeira vez e isso levou dias. Nenhuma postagem minha foi respondida.

2.2  O software estava com problemas de crash todo o tempo:
O seguinte erro estava acontecento sem parar, a ponto de atrapahar severamente a execucao do trabalho:
Error: signal 11:
/home/k4n3d4/vrep/libv_rep.so(_Z11_segHandleri+0x28)[0x7f35e62fdac8]
/lib/x86_64-linux-gnu/libc.so.6(+0x354b0)[0x7f35ea1754b0]
/usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so(+0x24b633)[0x7f35b7263633]
/usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so(+0xce9ae)[0x7f35b70e69ae]
/usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so(+0xb900f)[0x7f35b70d100f]
/usr/lib/x86_64-linux-gnu/dri/nouveau_dri.so(+0xcad86)[0x7f35b70e2d86]
/home/k4n3d4/vrep/libv_rep.so(_ZN3ogl12drawRichTextEiiiRNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERSt6vectorIiSaIiEEiPfSB_+0x3fb)[0x7f35e64fc85b]
/home/k4n3d4/vrep/libv_rep.so(_ZN3ogl10drawButtonE6VPointS0_PfS1_S1_NSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEibifbiS1_P16CTexturePropertyPS0_SA_S9_+0xdd7)[0x7f35e64ff4c7]
/home/k4n3d4/vrep/libv_rep.so(_ZN12CButtonBlock12displayBlockEPib+0x4c5)[0x7f35e64ec955]
/home/k4n3d4/vrep/libv_rep.so(_ZN21CButtonBlockContainer16displayAllBlocksEib+0x1b2)[0x7f35e6277e72]
QMutex: destroying locked mutex

2.3 Diferentes versoes do V-REP apresentando diferentes ferramentas:
A substituicao de algumas ferramentas ao longo da atualizacao do V-REP fez com que o pouco conteudo disponibilizado para aprendicado fosse limitado ainda mais pois os tutoriais disponiveis apresentavam solucoes em ferramentas que ja haviam sido descontinuadas. Exemplos que posso citar: path finding e o plugin de integracao com o ROS.


===============================================
CONSIDERACOES FINAIS
===============================================
Apesar de nao ter conseguido completar a implementacao da solucao, gostaria de agradecer a oportunidade a todos os envolvidos no projeto. obrigado.









