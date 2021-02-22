#!/bin/bash

# Set the Alpaca environment variables to the live trading values.

echo "Setting Alpaca Live Environment"
export APCA_API_BASE_URL=$APCA_API_BASE_URL_LIVE
export APCA_API_KEY_ID=$APCA_API_KEY_ID_LIVE
export APCA_API_SECRET_KEY=$APCA_API_SECRET_KEY_LIVE
