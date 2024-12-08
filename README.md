# getaround-end-to-end-rental-solution


## USAGE

Click on this link to access the web dashboard:
https://getaround-end-to-end-rental-solution-fxcfy9ndwnqd3facsw3nd5.streamlit.app/


## TRAINING

To train the model, run this command:

```py
python -m train
```

The model is saved in `data/model.pkl`.

## LOCAL DEPLOYMENT

```bash
cd deployment
```

```bash
streamlit run dashboard.py
```

```bash
python main.py
```

Or if you can use `make`:

```bash
make local-app
```
