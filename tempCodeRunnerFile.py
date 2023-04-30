from flask import Flask
from flask import request,render_template,redirect,url_for,send_file
import os,sys
from pdf2docx import parse
from typing import Tuple
from tkinter import t,messagebox
from tkinter import _tkinter