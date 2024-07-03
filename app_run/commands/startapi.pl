use Sys::Hostname;


my $hostname = hostname();

print("Running $hostname");

if ($hostname == 'app1')
{
    system("uvicorn app.api:app --host=0.0.0.0 --port=8000 --reload");

}
elsif($hostname == 'app2')
{
    system("uvicorn app.api:app --host=0.0.0.0 --port=8015 --reload");
}