import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService
public class CurrencyConverter {

    @WebMethod
    public double dollarsToRupees(double dollars) {
        // Assuming 1 Dollar = 74 Rupees (for example)
        double rupees = dollars * 74;
        return rupees;
    }
}
