---crear ambiente virtual
python -m venv myenv

---activar ambiente virtual
.\myenv\Scripts\activate


---actualizar pip
python.exe -m pip install --upgrade pip

---instalar mysql conector
python -m pip install mysql-connector-python

docker-compose -f .\docker-compose-mysql.yml up -d
docker run --name planeta -e MYSQL_ROOT_PASSWORD=0000 -p 3306:3306 -d mysql:latest
