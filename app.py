docenti = ["ABBONDANZA NICOLETTA",
 "AMENDOLA SERENA", 
 "ANDRETTI ELISABETTA", 
 "ANTARIDI SARA", 
 "BARAGHINI ANNALISA", 
 "BARONIO BARBARA", 
 "BENINI BARBARA", 
 "BIONDI CARLO", 
 "BISACCHI ANTONELLA", 
 "BOCCHINI MARCELLO", 
 "BRANDOLINI ELENA", 
 "BRIGHI ALBERTO", 
 "CANDUCCI LEONARDO", 
 "CARANO STEFANIA", 
 "CARLUCCI ADRIANO", 
 "CASADEI ELENA", 
 "CASADEI LUCA", 
 "CASILE ROBERTA", 
 "CASTAGNOLI ENRICO", 
 "COMELLI PIERO", 
 "CRASCI CARMELO", 
 "CRUCIANO MARCELLO", 
 "DALL'ARA JACOPO", 
 "DANESI ANTONIO", 
 "DI SAVINO SILVIO", 
 "FAGIOLI ENRICO", 
 "FERRARO GRAZIELLA", 
 "FILOMENA FRANCESCO", 
 "FORTI ELISA", 
 "FOSCHI LORENZO", 
 "FOSCHINI ANDREA", 
 "FUSAROLI CHIARA", 
 "GAGLIARDI ELEONORA", 
 "GALLINUCCI MORENA", 
 "GAMBERONI MATTEO", 
 "GARDELLI MARIA GRAZIA", 
 "GASPERONI PAOLA", 
 "GIOVANNINI VALENTINA", 
 "GORRASI ROSAMARIA", 
 "GRADARA SARA", 
 "GRECO TONI", 
 "GUADAGNO GRAZIA", 
 "GUALTIERI THOMAS", 
 "LENZI BARBARA", 
 "LUCCHI ARIANNA", 
 "LUCCHI GIANNI", 
 "LUCCHI MATTEO", 
 "LUMINI CINZIA", 
 "LUMINI PAOLO", 
 "MAZZOTTI IVAN", 
 "MELAGRANATI LORENZO", 
 "MINGOZZI CATIA", 
 "MOLARA FEDERICO", 
 "MONFREDA VITO", 
 "MONTALTI GIOVANNI", 
 "MUSCILLO ANTONIETTA", 
 "NICOLAI MASSIMO", 
 "NOVELLI ALESSANDRO", 
 "NUCCI SIMONE", 
 "OLANDESE PASQUALE", 
 "ORDINELLI ALESSANDRA", 
 "ORFEI MARCO", 
 "PARINI EMANUELE", 
 "PIETROPINTO CARMELINA", 
 "PIRACCINI ELENA", 
 "PIRACCINI FRANCESCA", 
 "PULGA LUCA", 
 "RONDONI FRANCESCO", 
 "RUSSO ANNAMARIA", 
 "RUSSOTTO ALESSANDRO", 
 "SERVADEI EMMANUELE", 
 "SICA ERMINIA", 
 "SINTUZZI MAURIZIO", 
 "SIROTTI GIULIANA", 
 "SOLOMITA PASQUALINO", 
 "SPIRITO FILIPPO", 
 "STELLA QUINTO PIO", 
 "SUCCI GRAZIELLA", 
 "TAGARELLI GIACOMO", 
 "TAPPI FRANCESCO", 
 "TEODORANI FEDERICO", 
 "TONELLI ALBERTO", 
 "TONETTI TIBERIO", 
 "TONINI TIZIANO", 
 "TORELLI GIACOMO", 
 "TUCCILLO MARIA GRAZIA", 
 "VACCARI ANDREA", 
 "VACCARI BERNARDO", 
 "VALDINOSI MICHELE", 
 "VALENTI ENRICO", 
 "VALZANIA SUSI", 
 "VENDRAMINETTO LAURA", 
 "VENETI DAVID", 
 "VENTURI FRANCESCO", 
 "VOLTA ALESSANDRA", 
 "ZAMPIGA MONICA", 
 "ZANARINI LAURA", 
 "ZANI LARA", 
 "ZOFFOLI LORENZO"]

for d in docenti:
    with open(f'{d}.json', 'w') as f:
        f.write("""{
    "orario": [
        {
            "Lun": {
                "I": null,
                "II": null,
                "III": null,
                "IV": null,
                "V": null,
                "VI": null
            }
        },
        {
            "Mar": {
                "I": null,
                "II": null,
                "III": null,
                "IV": null,
                "V": null,
                "VI": null
            }
        },
        {
            "Mer": {
                "I": null,
                "II": null,
                "III": null,
                "IV": null,
                "V": null,
                "VI": null
            }
        },
        {
            "Gio": {
                "I": null,
                "II": null,
                "III": null,
                "IV": null,
                "V": null,
                "VI": null
            }
        },
        {
            "Ven": {
                "I": null,
                "II": null,
                "III": null,
                "IV": null,
                "V": null,
                "VI": null
            }
        },
        {
            "Sab": {
                "I": null,
                "II": null,
                "III": null,
                "IV": null,
                "V": null
            }
        }
    ]
}""")
