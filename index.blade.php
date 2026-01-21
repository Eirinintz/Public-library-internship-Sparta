@extends('layouts.app')

@section('content')
<div class="card">
    <h2>Εξερχόμενα Έγγραφα</h2>

    <table border="1" width="100%" cellpadding="5">
        <thead>
        <tr>
            <th>Α/Α</th>
            <th>Αρχή στην οποία απευθύνεται</th>
            <th>Περίληψη</th>
            <th>Χρονολογία</th>
            <th>Σχετικοί Αριθμοί</th>
            <th>Φάκελος Αρχείου</th>
        </tr>
        </thead>

        <tbody>
        @forelse($documents as $doc)
            <tr>
                <td>{{ $doc->id }}</td>
                <td>{{ $doc->destination_authority }}</td>
                <td>{{ $doc->summary }}</td>
                <td>{{ $doc->document_date }}</td>
                <td>{{ $doc->related_numbers }}</td>
                <td>{{ $doc->file_folder }}</td>
            </tr>
        @empty
            <tr>
                <td colspan="6" align="center">Δεν υπάρχουν εγγραφές</td>
            </tr>
        @endforelse
        </tbody>
    </table>

    {{ $documents->links() }}
</div>
@endsection
