pragma solidity ^0.4.16;


contract Kalhatti {
    address public customer;
    address public merchant;
    address public loyality = 0x0A63Bce1Ea8457a2957a2F22770130bA2c8e78C0;

    enum Status {
        Success,
        Refunded
    }

    struct Transaction {
        address customer;
        address merchant;
        address loyality;
        uint amount;
        Status status;
    }

    Transaction[] public trxnList;
    mapping (address=>uint[]) public trxnMap;
    mapping (address=>uint256) public balance;

    modifier checkTrxnMerchant(address _merchant, uint256 id) {
        require(_merchant == trxnList[id].merchant);
        _;
    }

    modifier checkTrxnStatus(uint256 _id) {
        require(Status.Success == trxnList[_id].status);
        _;
    }

    function Kalhatti() public {
        customer = msg.sender;
        balance[customer] = 1000;
        transfer(0x3Df089557Cf684674E2AF27b68931B80bfDC9600, 100);
        transfer(0x3Df089557Cf684674E2AF27b68931B80bfDC9600, 100);
        transfer(0x3Df089557Cf684674E2AF27b68931B80bfDC9600, 100);
        transfer(0x3Df089557Cf684674E2AF27b68931B80bfDC9600, 100);
        transfer(0x3Df089557Cf684674E2AF27b68931B80bfDC9600, 100);
        refund(0x3Df089557Cf684674E2AF27b68931B80bfDC9600, 4);
        refund(0x3Df089557Cf684674E2AF27b68931B80bfDC9600, 3);
    }

    function balanceOf(address _owner) public view returns (uint256) {
        return balance[_owner];
    }

    function transfer(address _to, uint256 _value) public {
        balance[msg.sender] = safeSub(balance[msg.sender], _value);
        balance[loyality] = safeAdd(balance[loyality], _value/10);
        balance[_to] = safeAdd(balance[_to], (_value*9)/10);
        trxnList.push(Transaction(msg.sender, _to, loyality, _value, Status.Success));
        trxnMap[msg.sender].push(trxnList.length-1);
        trxnMap[_to].push(trxnList.length-1);
        trxnMap[loyality].push(trxnList.length-1);
    }

    function refund(address _merchant, uint256 id) public checkTrxnMerchant(_merchant, id) checkTrxnStatus(id) {
        Transaction storage trxn = trxnList[id];
        uint256 value = trxn.amount;
        balance[_merchant] = safeSub(balance[_merchant], (value*9)/10);
        balance[loyality] = safeSub(balance[loyality], value/10);
        balance[msg.sender] = safeAdd(balance[msg.sender], value);
        trxnList[id].status = Status.Refunded;

    }

    function safeSub(uint256 a, uint256 b) internal pure returns (uint256) {
        assert(b <= a);
        return a - b;
    }

    function safeAdd(uint256 a, uint256 b) internal pure returns (uint256 c) {
        c = a + b;
        assert(c >= a);
        return c;
    }
}