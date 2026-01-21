@extends('layouts.app')

@section('content')
<div class="card">
    <h2>Εισερχόμενα Έγγραφα</h2>

    <table border="1" width="100%" cellpadding="5">
        <thead>
        <tr>
            <th>Α/Α</th>
            <th>Ημερομηνία Παραλαβής</th>
            <th>Αριθμός Πρωτοκόλλου</th>
            <th>Τόπος που εκδόθηκε</th>
            <th>Αρχή που το εξέδωσε</th>
            <th>Χρονολογία εγγράφου</th>
            <th>Περίληψη</th>
            <th>Φάκελος Αρχείου</th>
        </tr>
        </thead>

        <tbody>
        @forelse($documents as $doc)
            <tr>
                <td>{{ $doc->id }}</td>
                <td>{{ $doc->incoming_date }}</td>
                <td>{{ $doc->protocol_number }}</td>
                <td>{{ $doc->place_issued }}</td>
                <td>{{ $doc->issuing_authority }}</td>
                <td>{{ $doc->document_date }}</td>
                <td>{{ $doc->summary }}</td>
                <td>{{ $doc->file_folder }}</td>
            </tr>
        @empty
            <tr>
                <td colspan="8" align="center">Δεν υπάρχουν εγγραφές</td>
            </tr>
        @endforelse
        </tbody>
    </table>

    {{ $documents->links() }}
</div>
@endsection

