int testar_tempo_atleta(double tempo){
    if (tempo <11.00){
        return 1;

    }

    else if (11.00<=tempo && tempo<12.00)
    {
        return 2;
    }
    
    else if (tempo>=12.00)
    {
        return 3;
    }
    

    return 0;
}