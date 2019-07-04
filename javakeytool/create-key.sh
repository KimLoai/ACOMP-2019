#!/bin/sh

KEYPASS=bkhpcc
STOREPASS=bkhpcc

echo "Generate server certificate and export it"
keytool -genkey -alias 10.28.8.70 -keyalg RSA -keypass $KEYPASS -storepass $STOREPASS -keystore keystore.jks
keytool -export -alias 10.28.8.70 -storepass $STOREPASS -file server.cer -keystore keystore.jks

echo "Create trust store"
keytool -import -v -trustcacerts -alias s10.28.8.70 -file server.cer -keystore cacerts.jks -keypass $KEYPASS -storepass $STOREPASS

