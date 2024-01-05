# prova 123

# ███╗   ███╗ █████╗ ███╗  ██╗████████╗██╗   ██╗  ██╗  ██╗ █████╗ ██╗     ██╗     
# ████╗ ████║██╔══██╗████╗ ██║╚══██╔══╝╚██╗ ██╔╝  ██║  ██║██╔══██╗██║     ██║     
# ██╔████╔██║██║  ██║██╔██╗██║   ██║    ╚████╔╝   ███████║███████║██║     ██║     
# ██║╚██╔╝██║██║  ██║██║╚████║   ██║     ╚██╔╝    ██╔══██║██╔══██║██║     ██║     
# ██║ ╚═╝ ██║╚█████╔╝██║ ╚███║   ██║      ██║     ██║  ██║██║  ██║███████╗███████╗
# ╚═╝     ╚═╝ ╚════╝ ╚═╝  ╚══╝   ╚═╝      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝


# LIBRERIA DA UTILIZZARE
import random


# DECISIONI CHE IL GIOCATORE PUO' PRENDERE
# Ci sono tre opzioni disponibili:
# 0 = NON CAMBIA MAI la sua opzione
# 1 = CAMBIA SEMPRE la sua opzione
# 2 = SCELTA RANDOM riguardo la sua opzione



# CREO UNA FUNZIONE PER FAR IL GIOCO
def gioco_monty_hall(numero_interazioni_gioco,tipologia_opzione_che_ha_il_giocatore) :
    
    # IMPOSTAZIONI BASE GIOCO
    vittorie_giocatore = 0
    vittorie_presentatore = 0

    for i in range(numero_interazioni_gioco):
        
        # GENERO ELEMENTI INIZIALI
        opzioni_possibili = [1,2,3]
        numero_vincente = random.choice([1,2,3])
        opzione_che_ha_il_giocatore = random.choice([1,2,3])
        
        #  TURNO DEL PRESENTATORE
        opzioni_disponibili_al_presentatore = [x for x in opzioni_possibili if x != opzione_che_ha_il_giocatore]
        cosa_il_presentatore_puo_aprire = [x for x in opzioni_disponibili_al_presentatore if x != numero_vincente]
        cosa_il_presentatore_apre = random.choice(cosa_il_presentatore_puo_aprire)
        opzioni_disponibili_al_presentatore.remove(cosa_il_presentatore_apre)
        opzione_restante_al_presentatore = opzioni_disponibili_al_presentatore[0]
        
        # QUI VALUTO LA TIPOLOGIA DI GIOCO CHE IL GIOCATORE STA GIOCANDO
        if tipologia_opzione_che_ha_il_giocatore == 0:
            cosa_il_giocatore_decide_alla_fine = 0
        elif tipologia_opzione_che_ha_il_giocatore == 1:
            cosa_il_giocatore_decide_alla_fine = 1
        elif tipologia_opzione_che_ha_il_giocatore == 2:
            cosa_il_giocatore_decide_alla_fine = random.choice([0,1])
        
        # Execute change of ball if necessary to do so
        if cosa_il_giocatore_decide_alla_fine == 1:
            variabile_momentanea = opzione_che_ha_il_giocatore
            opzione_che_ha_il_giocatore = opzione_restante_al_presentatore 
            opzione_restante_al_presentatore = variabile_momentanea
        
        # RISULTATO FINALE DEL GIOCO E PUNTEGGI
        if opzione_che_ha_il_giocatore == numero_vincente:
            vittorie_giocatore = vittorie_giocatore + 1
        elif opzione_restante_al_presentatore == numero_vincente:
            vittorie_presentatore = vittorie_presentatore + 1
    
    numero_round_giocati = vittorie_giocatore + vittorie_presentatore
    percentuale_vincita_giocatore = 100 * (vittorie_giocatore / numero_round_giocati)
    share_winning_presentatore = 100 * (vittorie_presentatore / numero_round_giocati)
    print('')
    print('Vincite del giocatore:',vittorie_giocatore,'| Percentuale vincita:',percentuale_vincita_giocatore,'%')
    print('Vincite del presentatore:',vittorie_presentatore,'| Percentuale vincita:',share_winning_presentatore,'%')

