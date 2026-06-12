import java.util.Scanner;

public class segundo_codigo_em_java {
    
    public static void main(String[]args){
        Scanner teclado = new Scanner(System.in);


        System.out.println("Digite seu nome");
        String cliente= teclado.next();
    
        System.out.println("Insira a quantidade");
        int quantidade = teclado.nextInt();

        double preco_produto = 37.8;
        //double preco_produto = teclado.nextDouble();//tem que ser usado "," nao ponto "."
        //System.out.println(quantidade * preco_produto);


       // System.out.println("ola seja muito bem vindo "+cliente);

        System.out.println("ola: "+cliente +" você comprou 10 itens, o total a pagar é: "+ preco_produto*quantidade+" reais" );
        //formatação//
        System.out.printf("%.2f",preco_produto*quantidade);
       teclado.close();
    }
}