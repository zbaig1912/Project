<template>
    <ul class="list-group" >
        <li class="list-group-item" v-for="item in data">{{item.key}}           :           {{item.value}}</li>
    </ul>
</template>

<script>
    import axios from 'axios';
    export default{
        props : {
            id : Number,
            cell: String
        },
        data(){
            return{
                headers:[],
                data:[]
            }          
        },
        methods:{
            getHeaders(){
                let cellClicked = "";
                let id = 0;
                cellClicked = this.cell;
                id = this.id
                if(cellClicked == "UserName"){
                    axios.get("/users/"+id).then(response => {
                        let user_data=[];
                        user_data = response.data;
                        this.data=[{key:"ID", value:user_data["id"]},{key:"NAME", value:user_data["name"]},{key:"EMAIL", value:user_data["email"]},{key:"FIRM", value:user_data.firm["name"]}];
                });
                }
                else if(cellClicked == "FirmName"){
                    axios.get("/firm/"+id).then(response => {
                        let user_data=[];
                        user_data = response.data;
                        this.data=[{key:"ID", value:user_data["id"]},{key:"NAME", value:user_data["name"]}];
                });
                }
                else if(cellClicked == "ProductName"){
                    axios.get("/product/"+id).then(response => {
                        let user_data=[];
                        user_data = response.data;
                        this.data=[{key:"ID", value:user_data["id"]},{key:"NAME", value:user_data["name"]}, {key:"PRICE", value:user_data["price"]}];
                });
                }
            },

        },
        created(){
            this.getHeaders(this.cell);
        }


    }
</script>
