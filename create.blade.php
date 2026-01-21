@extends('layouts.app')

@section('content')

<style>
    .doc-page {
        width: 100%;
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .doc-container {
        width: 1100px; /* σταθερό πλάτος για τέλειο κεντράρισμα */
        margin: 0 auto;
    }

    .doc-wrapper {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 30px;
    }

    .doc-box {
        width: 480px;
        background: #ffffff;
        border: 2px solid #000;
        padding: 25px 30px;
        border-radius: 6px;
    }

    .doc-title {
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 25px;
        text-decoration: underline;
    }

    .doc-box label {
        font-weight: bold;
        margin-bottom: 4px;
    }

    .doc-box input,
    .doc-box textarea {
        width: 100%;
        border: 1px solid #000;
        height: 32px;
        margin-bottom: 15px;
        padding-left: 6px;
    }

    .doc-box textarea {
        height: 90px;
        padding-top: 6px;
    }

    .save-btn {
        width: 100%;
        background: #000;
        color: #fff;
        padding: 10px;
        font-weight: bold;
        border: none;
        margin-top: 10px;
    }
</style>

<div class="doc-page">
    <div class="doc-container">

        <div style="text-align: center; margin: 40px 0;">
            <h2 class="fw-bold mb-4" style="font-size:2.2rem;">
                Συμπλήρωση Εγγράφων
            </h2>
        </div>

        <div class="doc-wrapper">

            <!-- ΕΙΣΕΡΧΟΜΕΝΑ -->
            <div class="doc-box">
                <div class="doc-title">ΕΙΣΕΡΧΟΜΕΝΑ ΕΓΓΡΑΦΑ</div>

                <form action="{{ route('incoming.store') }}" method="POST">
                    @csrf

                    <label class="form-label">Α/Α</label>
                    <input type="number" name="protocol_number" class="form-control" required>

                    <label class="form-label">Ημερομηνία Παραλαβής</label>
                    <input type="date" name="incoming_date" class="form-control" required>

                    <label class="form-label">Αριθμός Εισερχομένου Εγγράφου</label>
                    <input type="text" name="incoming_protocol" class="form-control" required>

                    <label class="form-label">Τόπος Έκδοσης</label>
                    <input type="text" name="sender" class="form-control">

                    <label class="form-label">Αρχή Έκδοσης</label>
                    <input type="text" name="subject" class="form-control">

                    <label class="form-label">Χρονολογία Εγγράφου</label>
                    <input type="date" name="document_date" class="form-control">

                    <label class="form-label">Περίληψη</label>
                    <textarea name="summary" class="form-control"></textarea>

                    <label class="form-label">Φάκελος Αρχείου</label>
                    <input type="text" name="comments" class="form-control">


                    <button class="save-btn">Αποθήκευση Εισερχομένου</button>
                </form>
            </div>

            <!-- ΕΞΕΡΧΟΜΕΝΑ -->
            <div class="doc-box">
                <div class="doc-title">ΕΞΕΡΧΟΜΕΝΑ ΕΓΓΡΑΦΑ</div>

                <form action="{{ route('outgoing.store') }}" method="POST">
                    @csrf

                    <label>Α/Α</label>
                    <input type="number" name="protocol_number" required>

                    <label>Αρχή στην οποία απευθύνεται</label>
                    <input type="text" name="sender" required>

                    <label>Περίληψη Εξερχομένου Εγγράφου</label>
                    <textarea name="summary"></textarea>

                    <label>Χρονολογία</label>
                    <input type="date" name="document_date">

                    <label>Σχετικοί Αριθμοί</label>
                    <input type="text" name="incoming_document_number">

                    <label>Φάκελος Αρχείου</label>
                    <input type="text" name="incoming_protocol">

                    <label>Παρατηρήσεις</label>
                    <textarea name="comments"></textarea>


                    <button class="save-btn">Αποθήκευση Εξερχομένου</button>
                </form>
            </div>

        </div>
    </div>
</div>

@endsection
