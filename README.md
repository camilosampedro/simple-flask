# simple-flask

Try it in Docker easily:

```bash
sudo docker run -p 5013:5000 -v "$(pwd):/repo" -it python bash
cd /repo
pip install -r requirements.txt
python app.py
```
