#!/bin/bash

# Set the Alpaca environment variables to the paper trading values.

echo "Setting Alpaca Paper Environment"
export APCA_API_BASE_URL=$APCA_API_BASE_URL_PAPER
export APCA_API_KEY_ID=$APCA_API_KEY_ID_PAPER
export APCA_API_SECRET_KEY=$APCA_API_SECRET_KEY_PAPER
