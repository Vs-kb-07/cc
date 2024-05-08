[webMethod]
public double D2R(Double doller)
{
    double ans=doller *82;
    return ans;
}
[webMethod]
public double R2D(Double rupees)
{
    double ans=rupees /82;
    return ans;
}
###############
@PUT
@Consumes(MediaType.TEXT_HTML)
@Path("/Uppercase")
public String toUppercaseMethod(String str)
{
    return str.toUpperCase();
}
@PUT
@Consumes(MediaType.TEXT_HTML)
@Path("/Lowercase")
public String toLowercaseMethod(String str)
{
    return str.toLowerCase();
}
