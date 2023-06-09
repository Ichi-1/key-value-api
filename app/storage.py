"""Инициализая key-value хранилища"""
import pickledb

storage = pickledb.load('embedded.db', auto_dump=True)