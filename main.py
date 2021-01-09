#!/usr/bin/env python3
from pyln.client import Plugin
import os
import sqlite3

plugin = Plugin(dynamic=False)

def copy(orig, dest):
    cursor = orig.cursor()
    cursor.execute("SELECT * FROM utxoset LIMIT 1;")
    records = cursor.fetchall()
    for row in records:
        c = dest.cursor()
        print(row)
        c.execute("INSERT INTO utxoset (txid, outnum, blockheight, spendheight, txindex, scriptpubkey, satoshis) VALUES (?,?,?,NULL,?,NULL,?)", 
                [ row[0], row[1], row[2], row[4], row[6]])
        c.close()
    cursor.close()

@plugin.method("utxoimport")
def utxoimport(plugin, inputfile):
    print("dbfile: " + plugin.dbfile)
    print("input file: " + inputfile)
    orig = sqlite3.connect(inputfile)
    dest = sqlite3.connect(plugin.dbfile)
    copy(orig, dest)
    dest.commit()
    dest.close()
    orig.close()
    return ""


@plugin.init()
def init(options, configuration, plugin):
    plugin.log("Plugin utxoset importer initialized")
    plugin.dbfile = os.path.join(configuration['lightning-dir'],
                                     "lightningd.sqlite3")

plugin.run()
