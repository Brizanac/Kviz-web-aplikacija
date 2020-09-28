import sqlite3
import uuid

def create_connection():
    try:
        db = sqlite3.connect('baza.db')
        return db
    except:
        return None

def prijava(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Korisnik WHERE username = ? AND password = ? ", (username, password))
    _korisnik = cursor.fetchone()
    korisnik = list(_korisnik)
    conn.close()
    return korisnik

def registracija(ime, prezime, username, password, email):
    conn = create_connection()
    cursor = conn.cursor()
    korisnik_id = uuid.uuid4().hex
    cursor.execute("INSERT INTO Korisnik (id, ime, prezime, username, password, email) VALUES (?, ?, ?, ?, ?, ?)", (korisnik_id, ime, prezime, username, password, email))
    conn.commit()
    conn.close()
    return korisnik_id


def dohvatiPitanja(kategorija_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pitanja WHERE id_kat = ?", (kategorija_id,))
    _pitanja = cursor.fetchall()
    pitanja = list(_pitanja)
    conn.close()
    return pitanja

def dohvatiOdgovore(pitanje_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Odgovori WHERE id_pit = ?", (pitanje_id,))
    odgovori = cursor.fetchall()
    conn.close()
    return odgovori
