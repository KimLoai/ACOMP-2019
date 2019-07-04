host=10.28.8.70
port=19090
echo -n | openssl s_client -showcerts -connect $host:$port  2>/dev/null  | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' >> serverp.cer
curl -X POST --data '{"id":1,"first_name":"Jameson","last_name":"Wyley","email":"jwyley0@sfgate.com"}' --cacert ./serverp.cer
