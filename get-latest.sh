git clone https://github.com/justJay-dev/python-safer.git

cp -r python-safer/safer/. safer/
cp python-safer/requirements.txt .
rm -r python-safer

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
