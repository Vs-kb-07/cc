import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService
public class LargestNumber {

    @WebMethod
    public int findLargest(int n1, int n2) {
        if (n1 > n2) {
            return n1;
        } else {
            return n2;
        }
    }
}
########################################3333
import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService
public class Factorial {

    @WebMethod
    public int calculateFactorial(int number) {
        int factorial = 1;
        for (int i = 1; i <= number; i++) {
            factorial *= i;
        }
        return factorial;
    }
}
#####################################
