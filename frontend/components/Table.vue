<template >
    <table id="tableComponent" class="table table-bordered table-striped">
        <thead>
            <tr>
                <!-- loop through each value of the fields to get the table header -->
                <th v-for="head in headers" :key='head'> {{head}} </th>
            </tr>
        </thead>
        <tbody v-for="row in rows" >
            <tr :class="{ opened: opened.includes(row.id) }">
                <td @click="toggle(row.id)">{{ row.name }}</td>
                <td>{{ row.handle }}</td>
                <td>{{ row.email}}</td>
                <td @click="toggle(row.id)">{{ row.firm}}</td>
            </tr>
            <tr v-if="opened.includes(row.id)">
                <td colspan="2">ON!</td>
            </tr>
        </tbody>
    </table>
</template>


<script>
export default{
    data() {
        return{
            headers:['ID', 'Name', 'Email', 'Firm'],
            opened: [],
            rows: [
            { id: 1, name: 'Bill', handle: 'bill', email: 'xyz@gmail.com', firm: 'Google'},
            { id: 2, name: 'Bob', handle: 'bob', email: 'abc@gmail.com', firm: 'Facebook' },
            { id: 3, name: 'Jim', handle: 'jim', email: 'ere@gmail.com', firm: 'Amazon' },
            { id: 4, name: 'Leroy', handle: 'leroy', email: 'egr@gmail.com', firm: 'Google' }
            ]
        }
        
    },
    methods: {
        toggle(id) {
            const index = this.opened.indexOf(id);
            if (index > -1) {
                this.opened.splice(index, 1)
            } else {
                this.opened.push(id)
            }
        }
    }
}
</script>

<style>
table {
  width: 100%;
  border: 1px solid #ccc;
}
td {
  padding: 2px;
  border: 1px solid #ccc;
}
.opened {
  background-color: yellow;
}
</style>


