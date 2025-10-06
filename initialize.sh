#!/usr/bin/env bash

SRC_FILE=$1   # 첫 번째 입력받은 파일명
NEW_FILE=$2   # 두 번째 입력받은 파일명
DEST_DIR="./acmicpc.net/"  # 이동할 디렉토리 지정

# 파일 이동
mv "$SRC_FILE" "$DEST_DIR"

# 새로운 파일 생성
touch "$NEW_FILE"

echo "Moved $SRC_FILE to $DEST_DIR"
echo "Created $NEW_FILE"