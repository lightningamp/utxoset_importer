# Utxoset importer plugin for c-lightning

This plugin allows to manually import one or more utxoset from another `lightning.sqlite3` in the current environment.

Enable plugin in your lightnigd instance and run the utxoimport command:
```bash
lightning-cli --testnet utxoimport /Users/luca/lightningd.sqlite3
```
