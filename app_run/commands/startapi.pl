use Sys::Hostname;


my $hostname = hostname();

print("Running $hostname");

if ($hostname eq 'app1')
{
    exec("uvicorn app.api:app --host=0.0.0.0 --port=8000 --reload");

}
elsif($hostname eq 'app2')
{
    exec("uvicorn app.api:app --host=0.0.0.0 --port=8015 --reload");
}