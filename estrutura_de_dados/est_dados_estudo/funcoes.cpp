bool testador_primo( int primo){

if (primo <2){
    return false;
}


for (int i = 2; i *i <= primo; i++)
{
    if (primo %i ==0 )
    {
        return false;
    }
    
}

return true;


}